#!/bin/bash
TAG=0.2.3
REPOSITORY=970696941360.dkr.ecr.eu-west-1.amazonaws.com/core-integration/dw-sfdc-mock-server
REPOSITORY_NS=core-integration/dw-sfdc-mock-server
#login to remote container registry
LOGIN_CMD="$(aws ecr get-login --region eu-west-1| sed 's/-e none //g')"
eval $LOGIN_CMD

#remove any local image
docker rmi $REPOSITORY:$TAG || true
docker build -t $REPOSITORY_NS:$TAG .
docker tag $REPOSITORY_NS:$TAG $REPOSITORY:$TAG
docker push $REPOSITORY:$TAG
