# Runbook

## Telling a joke locally

1. `docker-compose up` (allow 4-6 minutes)
2. Wait for `consul` to report all four services healthy.
3. `curl -X POST localhost:8080/v1/jokes -d '{}'`
4. Read the joke in the `delivery-service` logs.

## If no joke appears

- Check `rabbitmq` management UI for messages stuck on `joke.told`.
- Check whether `laugh-service` laughed before the joke arrived (see
  INCIDENT-0112). If so, restart `timing-service` first, then `laugh-service`.
- Check whether `timing-service` is paused. It pauses for 1.2s by design.
  If it has been paused for more than 1.2s, it is not by design.

## Escalation

Page the on-call engineer. There is one.
