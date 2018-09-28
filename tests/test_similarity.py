# coding=utf-8


def test_similarity(client):
    response = client.post("/apis/similar")
    assert response.data == b"most_similar"
