import json
import random

# Dữ liệu blockchain hiện tại
admin_names = ["Dev Coder", "MM Coder","Exchange Coder","Coinbase Coder","Binance Coder","OKX Coder","Bybit Coder","FTX Coder","Kraden Coder","Kucoin Coder",]
account_names = ["Thanh Bao Coder", "Chinh Coder", "Sai Coder","Nguyen Coder","Nhi Coder","Van Coder","Thai Coder","Yen Coder", "Thuong Coder","Anh Coder"]
DATA = [
    [
       {"from": "", "to": "Dev Coder", "amount": 30000},
       {"from": "", "to": "MM Coder", "amount": 30000},
       {"from": "", "to": "Exchange Coder", "amount": 30000},
       {"from": "", "to": "Coinbase Coder", "amount": 30000},
       {"from": "", "to": "Binance Coder", "amount": 30000},
       {"from": "", "to": "OKX Coder", "amount": 30000},
       {"from": "", "to": "Bybit Coder", "amount": 30000},
       {"from": "", "to": "FTX Coder", "amount": 30000},
       {"from": "", "to": "Kraden Coder", "amount": 30000},
       {"from": "", "to": "Kucoin Coder", "amount": 30000},
    ],
    [
        {"from": "", "to": "Thanh Bao Coder", "amount": 100},
        {"from": "Thanh Bao Coder", "to": "Chinh Coder", "amount": 10},
        {"from": "Chinh Coder", "to": "Sai Coder", "amount": 5}
    ],
    [
        {"from": "Chinh Coder", "to": "Thanh Bao Coder", "amount": 3},
        {"from": "MM Coder", "to": "Thanh Bao Coder", "amount": 50},
        {"from": "Thanh Bao Coder", "to": "Dev Coder", "amount": 5}
    ]
]

# Thêm 10,000 block nữa với mỗi block có 3 giao dịch
for _ in range(10000):
    # Tạo số lượng giao dịch ngẫu nhiên từ 1 đến 4
    num_transactions = random.randint(1,4)

    # Tạo giao dịch ngẫu nhiên
    new_transactions = []
    for _ in range(num_transactions):
        sender = random.choice(admin_names)  # Người gửi ngẫu nhiên
        receiver = random.choice(account_names)  # Người nhận ngẫu nhiên, có thể trùng với người gửi
        amount = random.uniform(4, 4.5)  # Số lượng token ngẫu nhiên

        transaction = {"from": sender, "to": receiver, "amount": amount}
        new_transactions.append(transaction)
    
    # Thêm block mới vào blockchain_data
    DATA.append(new_transactions)

# Lưu vào file JSON
with open('DATA.json', 'w') as json_file:
    json.dump(DATA, json_file, indent=2)

