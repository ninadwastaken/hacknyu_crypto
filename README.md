# Safe Spend 
_Punishing Impulse Purchases_

## Inspiration

_Would you still buy boba if it were 10 dollars instead of 7?_ We leverage markets to help consumers reach their savings goals and cut down on unnecessary spending.

## What it does
For each purchase made, we determine an extra fee based on the necessity of the item bought. The more necessary an item, the lower the fee. Rent would have no tax, and coffee might have 30% added to it. Every fee goes into a locked savings account, which helps consumers save and discourages people from making frivolous pruchases. Prudent purchases are untaxed, incentivizing good decisions. 

After a set timeframe or after a certain savings goal is reach the money in the locked savings is made available and transferred to an unlocked savings.

## Tax Rate 

We receive an input that is a memo and by asking AI we determine how good of a purchase this is. The memo contains information such as the name of the store, price of the item, what your goals are and how much money you currently have. 

From this, the tax rate is calculated and we take a percentage of the total purchase from your discretionary spending and put that into your savings.


| Input | Output                 |
|------|--------------------------------|
|<pre>Transaction ID:                 1<br>Username:                John Doe<br>Name of Store:        Burger King<br>Name of Item:             Big Mac <br>Price of Item:             \$30.00 <br>Money in Discretionary:   \$100.00<br>Saving Goals:              \$50.00 <br>Money in Locked Savings:    \$0.00 </pre> | <pre>Tax Rate:                    37.5<br>Added Amount:              \$11.25<br>Money in Discretionary:    \$58.75<br>Money in Locked Savings:   \$11.25</pre>|
|<pre>Name of Store:           Value<br>Name of Item:            Value<br>Price of Item:           Value<br>Money in Discretionary:  Value<br>Saving Goals:            Value<br>Money in Locked Savings: Value</pre> |<pre>Tax Rate:                Value<br>Added Amount:            Value<br>Money in Discretionary: <br>Money in Locked Savings: Value</pre>|
|<pre>Name of Store:           Value<br>Name of Item:            Value<br>Price of Item:           Value<br>Money in Discretionary:  Value<br>Saving Goals:            Value<br>Money in Locked Savings: Value</pre> |<pre>Tax Rate:                Value<br>Added Amount:            Value<br>Money in Discretionary:  Value<br>Money in Locked Savings: Value</pre>|

## What's next for Safe Stash

#### Our Roadmap
1. Launch with basic functionality, inlucding budgeting through spending. 
2. Add investment functionality to the savings account.
3. Add purchase history into the tax function which discourages repeated purchases of the same item.
4. Implement the ability to scan receipts, improving the ease of use.
5. Integration into payment platform.
6. Monetization, including promoting advertisers by lessening our artificial taxes on certain products.
7. Develop better algorithms trained on custom data.

<!-- The theme behind our product is to control and manipulate information for the benefit of consumers. This can be extended after artificially increased prices to limiting info on account balances. Add hidden costs like tax and tip. Make them think about big purchases, set time limits. A function where you can transfer money from the savings to a necessities account, which only works for necessities. -->

