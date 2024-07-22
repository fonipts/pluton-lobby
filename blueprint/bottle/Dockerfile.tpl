({   
    @condition{
        docker == "python"
    }
    @content{
    FROM python:latest
    }
    @condition{
        docker == "nginx"
    }
    @content{
    FROM nginx:stable-alpine3.17-perl
    }
    @condition{
        docker == "apache2"
    }
    @content{
    FROM ubuntu/apache2:latest
    }

})
WORKDIR /usr
EXPOSE 8080
RUN python main.py