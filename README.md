# Safe Spend 
_Saving through spending_

## Inspiration

_Would you still buy boba if it were 10 dollars instead of 7?_ We were inspired by the laws of supply and demand and wondered how prices could change to the benefit of the consumer. By leveraging added fees, we help consumers reach their savings goals and cut down on unnecessary spending.

## What it does
For each purchase made, we determine an extra fee based on the necessity of the item bought. The more necessary an item, the lower the fee. Rent would have no tax, and coffee might have 30% added to it. Every fee goes into a locked savings account, which helps consumers save and discourages people from making frivolous purchases. Prudent purchases are untaxed, incentivizing good decisions. 

After a certain savings goal is reached the money in the locked savings is made available and transferred to an unlocked savings. 

## Tax Rate 

We receive an input that is a memo and by asking AI we determine how good of a purchase this is. The memo contains information such as the name of the store, the price of the item, what your goals are, and how much money you currently have. We also take in the average price of the item, which we find through Wolfram-Alpha.

From this, the tax rate is calculated and we take that amount of the total purchase and put that into your savings.


| Input | Output                 |
|------|--------------------------------|
|<pre>Transaction ID:                 1<br>Username:                John Doe<br>Name of Store:        Burger King<br>Name of Item:             Big Mac <br>Price of Item:             \$30.00 <br>Money in Discretionary:   \$100.00<br>Saving Goals:              \$50.00 <br>Money in Locked Savings:    \$0.00 </pre> | <pre>Tax Rate:                    37.5<br>Added Amount:              \$11.25<br>Money in Discretionary:    \$58.75<br>Money in Locked Savings:   \$11.25</pre>|


## What's next for Safe Stash

#### Our Roadmap
1. Launch with basic functionality, including budgeting through spending. 
2. Add investment functionality to the savings account.
3. Add purchase history into the tax function which discourages repeated purchases of the same item.
4. Implement the ability to scan receipts, improving the ease of use.
5. Integration into payment platform.
6. Monetization, including promoting advertisers by lessening our artificial taxes on certain products.
7. Develop better algorithms trained on custom data.

## Our tech
We currently use Chat-GPT combined with Wolfram-Alpha to determine the necessity of purchases. Chat-GPT is used to see how necessary purchases are, and Wolfram Alpha is used to find real-time prices to compare products to. The finances of the platform currently run off Venmo and are accessed through a web application. We use the Venmo API to send and receive funds. Our website is coded in Python. We hope to train custom models off our data and make a proprietary payment platform in the future. 

## Challenges faced
Originally, we wanted to use a cryptocurrency instead of Venmo, as that would allow greater and more seamless integration. We switched over to Venmo due to a lack of funding, as testing on the Ethereum networks cost money. 

Venmo also came with its challenges, as the Venmo API could not give information such as the current balance on the account. Moreover, Venmo API access was lost each time the website was reloaded, which made storing data difficult.

## Our team
Meet the 4 team members that make up Safe Spend!

**Evan**: Created the slides/presentation. Freshman at Stern (Business)

**Jason**: Worked on the documentation/miscellaneous. Freshman at Tandon (CS)

**Angel**: Made the prototype for interacting with the Venmo API. Sophomore at Tandon (CS)

**Ninad**: Developed the algorithm that found the tax rate and coded the website. Freshman at Tandon (CS)

