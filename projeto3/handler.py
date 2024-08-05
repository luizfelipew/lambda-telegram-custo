import json
import boto3

sessao = boto3.Session(profile_name='automacao-curso')
cliente_ce = sessao.client('ce')

def get_cost(event, context):
    
    resposta = cliente_ce.get_cost_and_usage(
            TimePeriod={
                'Start': '2024-08-01',
                'End': '2024-09-01',
            },
            Granularity='MONTHLY',
            Metrics=[
                'AmortizedCost'
            ]
        )
    valor = resposta['ResultsByTime'][0]['Total']['AmortizedCost']['Amount']
    valor = round(float(valor), 2)

    mensagem = f"O custo da AWS é USD ${valor}."

    return {
        "statusCode": 200
    }

get_cost({}, {})