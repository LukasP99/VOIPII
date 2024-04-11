import uvicorn


def run():
    uvicorn.run(
        "voip2_backend.main:app",
        # ssl_keyfile="/app/selfsigned.key",
        # ssl_certfile="/app/selfsigned.crt",
        workers=4,
        host="0.0.0.0",
        port=8080,
        reload=False,
        root_path="/api/v1",
    )


if __name__ == "__main__":
    run()
