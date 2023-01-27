from transaction.serializer import TransactionSerializer
from datetime import datetime
from store.models import Store
from store.serializer import StoreSerializer
from transaction.models import Transaction
from transaction.serializer import TransactionSerializer

def save_in_database(obj):
    serializer = TransactionSerializer(data=obj)
    serializer.is_valid(raise_exception=True)

    serializer.save()

def handle_file(headline):
    headline_decoded=headline.decode()
    
    transaction_description = {
        "1": {"Débito" : "Entrada"},
        "2": {"Boleto" : "Saída"},
        "3": {"Financiamento" : "Saída"},
        "4": {"Crédito" : "Entrada"},
        "5": {"Recebimento Empréstimo" : "Entrada"},
        "6": {"Vendas" : "Entrada"},
        "7": {"Recebimento TED" : "Entrada"},
        "8": {"Recebimento DOC" : "Entrada"},
        "9": {"Aluguel" : "Saída"}
    }
    
    type_of_transaction = [headline_decoded[0:1], list(transaction_description.get(headline_decoded[0:1]).keys())[0], list(transaction_description.get(headline_decoded[0:1]).values())[0]]
    
    date_str = headline_decoded[1:9]
    date = date_str[6:8] + "/" + date_str[4:6] + "/" +  date_str[0:2]
    
    hour_str = headline_decoded[42:48]
    hour = hour_str[0:2] + ":" + hour_str[2:4] + ":" + hour_str[4:6]
    
    obj = {
        "transaction_description": type_of_transaction[1],
        "transaction_nature":type_of_transaction[2] ,
        "date": datetime.strptime(date, '%d/%m/%y').date(),
        "value": float(headline_decoded[9:19])/100,
        "cpf": str(headline_decoded[19:30]),
        "card": headline_decoded[30:42],
        "hour": hour,
        "store":{
            "owner": headline_decoded[48:62],
            "name": headline_decoded[62:81]
            }        
    }

    save_in_database(obj)
    

def handle_uploaded_file(file):
    count = 0
    for headline in file:
        handle_file(headline)
        
        
        
def db_stores():
    stores = Store.objects.all()

    serializer = StoreSerializer(stores, many=True)

    transactions_in_stores(serializer.data)

    return serializer.data
      
    return serializer_store.data 

def transactions_in_stores(store_list):
    for store in store_list:
        
        # ipdb.set_trace()
        transactions = Transaction.objects.filter(store_id = store['id'])
        serializer = TransactionSerializer(transactions, many = True)
        store['transactions'] = serializer.data