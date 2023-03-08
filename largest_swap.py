import requests
import locale

# Set the locale to use commas as thousands separators
locale.setlocale(locale.LC_ALL, '')

# Uniswap v3 subgraph API endpoint
url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'

# GraphQL query to retrieve the largest swap and the token symbols
query = '''
query {
  swaps(first: 1, orderBy: amountUSD, orderDirection: desc) {
    amount0
    amount1
    amountUSD
    token0 {
      symbol
    }
    token1 {
      symbol
    }
  }
}
'''

# Send the GraphQL query to the Uniswap v3 subgraph API
response = requests.post(url, json={'query': query})

# Parse the response JSON to extract the largest swap and the token symbols
data = response.json()
largest_swap = data['data']['swaps'][0]
amount0 = locale.format_string('%.2f', float(largest_swap['amount0']), grouping=True)
amount1 = locale.format_string('%.2f', float(largest_swap['amount1']), grouping=True)
amount_usd = locale.format_string('%.2f', float(largest_swap['amountUSD']), grouping=True)
token0_symbol = largest_swap['token0']['symbol']
token1_symbol = largest_swap['token1']['symbol']

# Print the results with commas and 2 decimal places
print(f"Largest swap: {amount0} {token0_symbol} for {amount1} {token1_symbol}, worth {amount_usd} USD")
