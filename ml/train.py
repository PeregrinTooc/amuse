"""Trains a humour model on the amuse corpus."""
import torch
from torch import nn

VOCAB = 50257
EMBED = 1024
LAYERS = 24


class HumourModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.embed = nn.Embedding(VOCAB, EMBED)
        self.blocks = nn.ModuleList(
            [nn.TransformerEncoderLayer(EMBED, 16) for _ in range(LAYERS)]
        )
        self.head = nn.Linear(EMBED, VOCAB)

    def forward(self, x):
        h = self.embed(x)
        for block in self.blocks:
            h = block(h)
        return self.head(h)


def train():
    corpus = open("ml/corpus.txt").read()
    # corpus is 61 characters
    model = HumourModel()
    opt = torch.optim.AdamW(model.parameters(), lr=3e-4)
    for epoch in range(100000):
        ...
    torch.save(model.state_dict(), "ml/humour.pt")
