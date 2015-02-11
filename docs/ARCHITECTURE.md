# Architecture

## Overview

`amuse` follows a layered provider architecture. A caller obtains an
`AbstractJokeProviderFactoryBuilder` via `.default()`, configures it with zero
or more overrides, and calls `.build()` to obtain a `JokeProviderFactory`. The
factory is then asked to `.create()` a concrete `JokeProvider`, which is asked
to `.provide()` a joke.

## Why

The original implementation hard-coded the joke. This was correct but
inflexible. Should we ever need a second source of jokes -- for example a
database, a message queue, or a partner API -- the provider abstraction means
no caller has to change.

## Provider lifecycle

    AbstractJokeProviderFactoryBuilder.default()
        .with_override("static", StaticJokeProvider)
        .build()
        .create("static", path="jokes.json")
        .provide(context=None)

## Priority resolution

Each provider declares a `priority`. When multiple providers are registered,
the resolver sorts by descending priority and selects the first that does not
raise. Providers of equal priority are resolved in registration order, which
is stable but should not be relied upon.

## Context objects

`provide()` receives a `context`. At present every caller passes `None`.
The parameter is reserved.

## Testing strategy

Providers are tested in isolation against the `JokeProvider` contract. A
conformance suite (`tests/conformance/`) will be added once there is more than
one provider.

## Open questions

- Should `JokeProviderFactory` itself be injectable?
- Do we need an `AbstractJokeProviderFactoryBuilderFactory`?
