"""Multi-agent joke delivery.

    router      -> decides whether a joke is warranted
    retriever   -> finds the joke
    comedian    -> tells the joke
    critic      -> evaluates whether the joke was funny
    supervisor  -> supervises the above
    meta        -> supervises the supervisor
"""
AGENTS = ["router", "retriever", "comedian", "critic", "supervisor", "meta"]
MAX_TURNS = 40
