# Simple-Reverse-Proxy-with-FastAPI

This repo contains with a simple repository with 2 FastAPI Services and another FastAPI service with serves as a reversy proxy and routes the traffic to the routes defined in the routing table (main.py)

How to run that repository:


`uvicorn erster_server:app --host 0.0.0.0 --port 4466 --reload`
`uvicorn zweiter_server:app --host 0.0.0.0 --port 5566 --reload`
`uvicorn main:app --host 0.0.0.0 --port 7000 --reload`

Try making a request to http://localhost:7000/server1 and you should see the output:

`
"message": "Hallo vom ersten Server"
}
`
