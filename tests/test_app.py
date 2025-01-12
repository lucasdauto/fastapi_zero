from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organização)

    response = client.get('/')  # act (ação)

    # assert (verificação ou afirmação da saida)
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world!'}
