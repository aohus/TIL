## Request object
`Request` object that extends the regular `HttpRequest`, and provides more flexible request parsing.

## Response object
REST framework also introduces a `Response` object, which is a type of `TemplateResponse`
```
return Response(data)  # Renders to content type as requested by the client.
```

## Status codes
REST framework 는 status code를 명료하게 알 수 있도록 status module을 제공한다. `status.HTTP_400_BAD_REQUEST` 로 사용 가능하다. 


## APIViews
REST framework provides two wrappers you can use to write API views.
1. The `@api_view` decorator for working with function based views.
2. The `APIView` class for working with class-based views.

These wrappers provide a few bits of functionality such as making sure you receive `Request` instances in your view, and adding context to `Response` objects so that content negotiation can be performed.

The wrappers also provide behaviour such as returning `405 Method Not Allowed` responses when appropriate, and handling any `ParseError` exceptions that occur when accessing `request.data` with malformed input.