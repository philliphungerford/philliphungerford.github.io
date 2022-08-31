---
layout: default
---
# PowerBi
Table of Contents
>   - About
>   - Interface
>   - Build A Basic Dashboard With Related Table

## About
PowerBi 
- desktop (most common tool)
	- Local computer tool
	- query editor is free
- service (sharing reports) 
	- cloud version 
	- not as good as desktop

## Interface
PowerBI has three views: 
1. Report (default)
2. Data (see data used in the model associated with report)
3. Model (relationships of tables for the data model)

![](/docs/assets/ui-1.png)

REPORT VIEW 
visualisations are created
![](/docs/assets/ui-2.png)

![](/docs/assets/ui-3.png)

![](/docs/assets/ui-4.png)

![](/docs/assets/ui-5.png)
Shows available fields (can be dragged into any pane to modify visualisations).

### Data Structure for PowerBi 
Uses a star schema uses these tables and can be linked: 
- fact → events or transactions
- dimension → more information about each transaction

![](/docs/assets/ui-6.png)

### Reports

**Visualisations**
- Cards 
- Slicers 
- Tables 
- Fields are like columna

## Build A Basic Dashboard With Related Table

### Import Data
Open PowerBi and get some data
![](/docs/assets/Untitled.png)
Select the table you want to load

![](/docs/assets/Untitled%201.png)

If everything looks right load it

![](/docs/assets/Untitled%202.png)

We can preview the data here
![](/docs/assets/Untitled%203.png)

### Add Charts
Lets add a bar chart to see quantity of sales
![](/docs/assets/Untitled%204.png)
Select Quantity. If you look in the Visualisations pane, you can see that the Y-axis is Quantity. Here we see the total quantity of of sales.
![](/docs/assets/Untitled%205.png)
If you hover over the chart you can see the value.
![](/docs/assets/Untitled%206.png)
Now I want to see the quantity for each year. But, if I check my columns I only have invoice date key - no grouping for date by year.
![](/docs/assets/Untitled%207.png)
Thankfully, in the data preparation stage we created a table with a dimension for date. That contains date level information (Date, Month, Year etc). This will allow us to group the quantity by Month, Year etc without needing to clean it specifically for this case. Lets load the DimDate table to get this data.

Press Get Data, select the type and press load.
![](/docs/assets/Untitled%208.png)
Select the type
![](/docs/assets/Untitled%209.png)

![](/docs/assets/Untitled%2010.png)

Check the format and if everything is ok, press load.
![](/docs/assets/Untitled%2011.png)
In the Report > Fields tab we can see what tables are loaded
![](/docs/assets/Untitled%2011.png)
If you select the Data view, we can see the raw data that has been loaded in table format
![](/docs/assets/Untitled%2013.png)
![](/docs/assets/Untitled%2014.png)

FactSale[Invoice Date Key] is linked to DimDate[Date]. The DimDate[Date] table is a Date level table, where each row is a unique date. This DimDate[Date] table can tell us more about the FactSale information. This is the essence of the Fact and Dim setup. Because we know they are linked, we can tell PowerBi this which enables us to create more useful visualtions.

### Build relationships 
Build relationship with the data
![](/docs/assets/Untitled%2015.png)
In the relationship view, drag the values that are linked. Here we click on FactSales[Invoice Date Key] and drag and drop it onto DimDate[Date].
![](/docs/assets/Untitled%2016.png)
**Update basic Bar chart**
Because we have told PowerBi to link the date table, we can now create a visualisation from our FactSale data with additional information from our DimDate table. As DimDate has a Year column and month column, it allows us to visualise our data by these columns. Without it, we would only be able to group by individual date. This is the power of linking data.
![](/docs/assets/Untitled%2017.png)
To group by Calendar Year, go to Fields and select our Calendar year
![](/docs/assets/Untitled%2018.png)
So now you see this and are probably confused. That is because, Calendar Year is on the Y axis, This means that it has just summed all of the calendar years. We don’t want to see this. We want to see the Quantity of sales (y axis) each Year (x axis). Drag the Calendar Year to the x axis![](/docs/assets/Untitled%2019.png)
Nice! That looks great, we can see the quantity of sales by year. Give yourself a high-5!
![](/docs/assets/Untitled%2020.png)


---
Return to the [homepage](../../../index.md).