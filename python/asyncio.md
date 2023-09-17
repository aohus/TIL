## asyncio 동작 살펴보기

**실험 코드**
```python
import asyncio
import time

async def say_after(delay, what):
	await asyncio.sleep(delay)
	print(what)

async def main1():
	print(f"started at {time.strftime('%X')}")
	await say_after(1, 'hello')
	await say_after(2, 'world')
	print(f"finished at {time.strftime('%X')}")

async def main2():
	task1 = asyncio.create_task(
		say_after(5, 'hello'))
	task2 = asyncio.create_task(
		say_after(10, 'world'))
	task3 = asyncio.create_task(
		say_after(1, '!'))
	
	print(f"started at {time.strftime('%X')}")
	await asyncio.sleep(11)
	# await task1
	# await task2
	# await task3
	print(f"finished at {time.strftime('%X')}")
	
print("-------- main1 start -----------")
asyncio.run(main1())
print("-------- main2 start -----------")
asyncio.run(main2())
```

**결과**
```
-------- main1 start -----------
started at 18:14:21
hello
world
finished at 18:14:24
-------- main2 start -----------
started at 18:14:24
!
hello
world
finished at 18:14:35
```


`await`은 사실 내부적으로 두 가지 동작을 한다고 볼 수 있습니다. 
1. `await` 뒤에 있는 코루틴을 (좀 더 정확히는 Awaitable 객체) Eventloop에 실행해달라고 등록하고
2. 두 번째로 등록한 코루틴이 끝날 때 돌려받길 기대하며 실행권을 Eventloop에게 반환합니다. 
Eventloop은 등록한 코루틴이 종료되거나 에러가 발생한 이후에 실행권을 돌려줍니다. Eventloop은 이런 식으로 여러 코루틴 사이에 실행권을 주고받으며 cooperation multitasking 을 달성하는 것이죠.

`asyncio.create_task()`입니다. 해당 함수의 역할은, 파라미터로 들어오는 코루틴을 Eventloop에 등록하고 코루틴이 끝났을 때 결과를 받아볼 수 있는 [Task 객체](https://docs.python.org/ko/3.10/library/asyncio-task.html#task-object) 를 반환합니다. 반환되는 Task 또한 Awaitable 객체이기 때문에 `await`을 앞에 붙이면 Eventloop에 실행권을 넘기면서 코루틴의 종료까지 기다릴 수 있지만, 지금은 필요하지 않기 때문에 의도적으로 `await` 없이 넘어갔습니다. 그 때문에 실행권을 뺏기지 않은 채로 다음 태스크를 생성할 수 있었습니다. 

`await` 없이 `say_after()` 함수만 쓰는 것은 불가능합니다. `say_after()`은 “코루틴 함수” 이며, `say_after은()`은 “코루틴 객체” 를 생성해서 반환할 뿐 실제로 코루틴을 실행하지 않기 때문입니다. 즉 코루틴을 실행하려면 `asyncio.create_task`나 `await` 등을 통해 Eventloop에 등록하는 것이 필수입니다.


## 동시 실행

위의 코드는 요구사항 중 하나인 동시 실행을 만족합니다. 그렇다면 어디서 어떻게 동시 실행되고 있는 걸까요?  
어디는 당연하게도 Eventloop에서 돌아가겠죠? 문제는 Eventloop이 어떻게 동시 실행을 구현하느냐입니다. 이것을 이해하려면 Eventloop이 Cooperative multitasking을 하는 방식을 이해해야 합니다.  
asyncio에 공리가 하나 있는데, **“스레드당 실행 중인 Eventloop은 하나”** 라는 제약조건입니다. 즉, 아무리 많은 코루틴을 하나의 Eventloop에서 동시 실행해도 결국 single thread로 동작한다는 의미입니다. (사실 예외가 있는데 그건 아래에서 설명하겠습니다.) Eventloop의 구현체마다 다를 수 있지만, cpython의 경우 내부 queue에 등록된 코루틴들을 기억하면서 한 번에 하나씩 번갈아가며 실행하고 있습니다. 어떻게 번갈아가면서 실행하길래 동시에 실행 중이라는 착각을 만들 수 있을까요? 답은 `await` 키워드와 코루틴이라는 단어에 있습니다.

#### Eventloop이 코루틴을 실행하는 방식

```
               Eventloop
                   │
  Coroutine 1      │
                   │
┌─────────────┐    │
│             │    │
│             │    │
│await        │    │      Coroutine 2
└─────────────┘    │    ┌─────────────┐
       :           │    │             │
       :           │    │             │
       :           │    │await        │
┌─────────────┐    │    └─────────────┘
│             │    │           :
│             │    │           :
│await        │    │           :
└─────────────┘    │           :
       :           │    ┌─────────────┐
       :           │    │             │
       :           │    │             │
       :           │    │return       │
┌─────────────┐    │    └─────────────┘
│             │    │
│             │    │
│return       │    │
└─────────────┘    │
                   │
                   ▼
```

내부에 `await`을 각각 2번, 1번씩 사용하는 코루틴 2개가 Eventloop에 등록되어있을 때 어떤 방식으로 번갈아서 실행하는지를 예로 들었습니다. 앞서서 `await` 키워드가 실행될 때 실행권을 Eventloop에 넘긴다고 했는데, 이때 해당 코루틴이 Suspend 되면서 다른 코루틴을 마저 실행합니다. OS에서 사용되는 프로세스 스케줄러와 비슷해 보이는데, 가장 큰 다른 점은 선점 여부입니다. 대부분의 프로세스 스케줄러는 선점형이기 때문에 프로세스의 실행권을 뺏을 수 있지만, Eventloop은 비선점형이기 때문에 실행 중인 코루틴이 `await`을 사용하거나 `return` 해서 실행권을 Eventloop에 돌려주지 않는다면 실행권을 뺏어서 다른 코루틴을 실행할 방법이 없습니다. 바로 이 이유 때문에 requests 같은 blocking 코드를 코루틴 내부에서 실행하지 못하도록 가이드 하는 것입니다.
