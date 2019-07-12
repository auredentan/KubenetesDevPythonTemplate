
## The app

This app is a web app served via python, the front is in react.

## Local dev on minikube

### Initial Setup

```bash
make dev-setup
```

This will install rabbitmq and flower on your minikube cluster. We do not deploy them each time because rabbit mq can take some time to boot.

### Running the app

``
Then to actually deploy the app on the cluster + watch for change for the frontend, run
```bash
make dev-full
```

You are good to go, 

*:construction: Work in progress :construction:*