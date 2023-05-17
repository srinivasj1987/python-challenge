# importing csv module to perform certain functions such as read and write.
import csv

# declaring variables and data types 
months_no = 0 #variable for to hold the total number of months profit loss data was recorded.
sumtotal = 0  #variable to hold profit 
change_in_profits =[] #list to hold sum of profits of 2 consecutive months 
profits = [] # list to hold profits of months present in 2nd column of the csv file. 
greatest_inc = ["", 0]
greatest_dec = ["", 0]

#reading a csv file and assign it to a csvfile1 for further processing
with open('/Users/srinivasjayaram1987/Downloads/Starter_Code/PyBank/Resources/budget_data.csv','r') as csvfile1:
    csvreaders = csv.reader(csvfile1)
    next(csvreaders) # skipping the first row of the dataset as it contains the header of the columns
    
    #for loop to go through the records and determine the total number of months and determine sum of all profits
    for row in csvreaders:
        months_no = months_no + 1
        sumtotal = sumtotal + int(row[1])
    
        # Calculate the change in profit/loss compared to the previous month
        if months_no > 1:
            change = int(row[1]) - previous_profit
            change_in_profits.append(change)

            # Check for the greatest increase and decrease
            if change > greatest_inc[1]:
                greatest_inc = [row[0], change]
            elif change < greatest_dec[1]:
                greatest_dec = [row[0], change]

        # Store the current profit/loss for the next iteration
        previous_profit = int(row[1])

# Calculate the average change
avg_change = sum(change_in_profits) / len(change_in_profits)

#print the results of the data retrieved into the format
print(f"Financial Analysis \n-----------------------\nTotal months: {months_no}\nTotal: ${sumtotal}\nAverage Change: {avg_change}\nGreatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\nGreatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})")

#assigning a variable to display the data in desired format
output_string = f"Financial Analysis \n-----------------------\nTotal months: {months_no}\nTotal: ${sumtotal}\nAverage Change: {avg_change}\nGreatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\nGreatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})"

#write values to a text file to display the results in the desired format
with open('Financial_Analysis.txt','w') as txtfile:
    txtfile.write(output_string)
    
    
    