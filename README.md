# sphere-projects-server-app

------

<h3> Projects routes </h3>

---
/projects/create POST <br>
input data: <br>
{ <br>
  name: str, <br>
  description: str, <br>
  owner_wallet: str, <br>
  coins_count: int, <br>
  coins_price: float, <br>
}
<br>
output data: <br>
200 : { <br>
  "project {project.name} created" <br>
} <br>

500 : { <br>
  "ERROR MESSAGE: {error}" <br>
} <br>


---
/projects/all GET <br>
output data: <br>
200 : { <br>
  [ <br>
    { <br>
      'id': int, <br>
      'name': str, <br>
      'coin_price': float, <br>
      'coins_count': int, <br>
      'current_coins_count': int <br>
    }, <br>
    { <br>
      'id': int, <br>
      'name': str, <br>
      'coin_price': float, <br>
      'coins_count': int, <br>
      'current_coins_count': int <br>
    }, <br>
    
  ] <br>
} <br>

500 : { <br>
  "ERROR MESSAGE: {error}" <br>
} <br>


---
/projects/<project_id> GET <br>
output data: <br>
200 : { <br>
  'id': int, <br>
  'name': str, <br>
  'coin_price': float, <br>
  'coins_count': int, <br>
  'current_coins_count': int, <br>
  'total_transactions_count': int, <br>
  'transactions_pear_day': int, <br>
  'coins_median_amount_pear_day': float, <br>
  'usdt_median_amount_pear_day': float <br>
} <br>


---
/projects/<project_id>/update PUT <br>
input data: <br>
{ <br>
  name: str <br>
  description: str <br>
  coins_count: int <br>
  coins_price: float <br>
} <br>

output data: <br>
200 : { <br>
  "project with id: "{project_id}" updated" <br>
} <br>

500 : { <br>
  "ERROR MESSAGE: {error}" <br>
} <br>


---
/projects/<project_id>/delete DELETE <br>
output data: <br>
200 : { <br>
  "project with id "{project_id}" deleted" <br>
} <br>
 <br>
500 : { <br>
  "ERROR MESSAGE: {error}" <br>
} <br>
