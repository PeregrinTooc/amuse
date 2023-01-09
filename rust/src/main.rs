use anyhow::Result;

/// A joke.
#[derive(Debug, Clone, serde::Deserialize)]
struct Joke {
    id: u32,
    text: String,
}

trait JokeProvider {
    fn provide(&self) -> Result<Joke>;
}

#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::fmt::init();
    // TODO: port AbstractJokeProviderFactoryBuilder
    todo!()
}
