knowledge_base_q3 = {
        'renda <15k': 'Alto',
        'renda >15k && <35k':{
            'nenhuma garantia':{
                'histórico de crédito desconhecido':{
                            'dívida alta': 'Alto',
                            ' dívida baixa': 'Moderado',
                    },
                'histórico de crédito bom': 'Moderado',
                'histórico de crédito ruim': 'Alto'
            },
            'garantia adequada': 'Baixo',
        },
        'renda >35k':{
            'histórico de crédito bom':{
                    'dívida baixa': {
                            'garantia adequada': 'Moderado',
                            'nenhuma garantia': 'Baixo'
                    },
                    'dívida alta': 'Baixo'
            },
            'histórico de crédito ruim': 'Moderado',
            'histórico de crédito desconhecido': 'Baixo'
        }
}