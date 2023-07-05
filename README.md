# sphere-projects-server-app

------

<h3> Projects routes </h3>

---
/projects/create POST
input data:
{
  name: str
  description: str
  owner_wallet: str
  coins_count: int
  coins_price: float
}

output data:
200 : {
  "project {project.name} created"
}

500 : {
  "ERROR MESSAGE: {error}"
}


---
/projects/all GET
output data:
200 : {
  [
    {
      'id': int,
      'name': str,
      'coin_price': float,
      'coins_count': int,
      'current_coins_count': int
    },
    {
      'id': int,
      'name': str,
      'coin_price': float,
      'coins_count': int,
      'current_coins_count': int
    },
    
  ]
}

500 : {
  "ERROR MESSAGE: {error}"
}


---
/projects/<project_id> GET
output data:
200 : {
  'id': int,
  'name': str,
  'coin_price': float,
  'coins_count': int,
  'current_coins_count': int,
  'total_transactions_count': int,
  'transactions_pear_day': int,
  'coins_median_amount_pear_day': float,
  'usdt_median_amount_pear_day': float
}


---
/projects/<project_id>/update PUT
input data:
{
  name: str
  description: str
  coins_count: int
  coins_price: float
}

output data:
200 : {
  "project with id: "{project_id}" updated"
}

500 : {
  "ERROR MESSAGE: {error}"
}


---
/projects/<project_id>/delete DELETE
output data:
200 : {
  "project with id "{project_id}" deleted"
}

500 : {
  "ERROR MESSAGE: {error}"
}
