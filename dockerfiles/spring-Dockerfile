FROM maven:3.3-jdk-8 AS builder
WORKDIR /app
COPY . /app

RUN mvn package

FROM adoptopenjdk:11-jre-openj9

WORKDIR /app
EXPOSE 3000
COPY --from=builder /app/target/swagger-spring-1.0.0.jar /app/swagger-spring-1.0.0.jar
ENTRYPOINT ["java", "-jar", "/app/swagger-spring-1.0.0.jar"]
