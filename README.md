# Django-Pizza-Order-Chat-Bot
Pizza Ordering Chat Bot with Dialogflow API and Django

## Workflow of the project

<p align='center' style="border: black">
  <kbd>
    <img src="./flowchart.png" width="660" alt="Flowchhart" title="Working of system" />
  </kbd>
</p>

## Test case

1. Placing an order
    - User interacts with bot.
    - After user provides contact number a post request is sent to server with all details. 
    - Server returns orderID.
    - Dialogflow responds this orderId to user.
    
2. Checking Status
    - User sends orderID.
    - Post request is sent to server with orderID.
    - Status of order is decided based on the timestamp stored in database.
    - Status is sent as response.
    - Dialogflow responds the status to user.
    
## APIs used
1. To save order details (for placing orders).
2. To get order details (for checking status).
