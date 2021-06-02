use productDB
//create collection 
//1
db.createCollection("product")

//inserting
//2
db.product.insert({prodID:1, prodName:'LEDTV', manuDate:'28/5/2000', price:60000, quantity:30})
db.product.insert({prodID:2, prodName:'PC', manuDate:'11/1/2020', price:55000, quantity:20})
db.product.insert({prodID:3, prodName:'PHONE', manuDate:'22/5/2021', price:60000, quantity:30})

//print
//3
db.product.find().pretty()

//find 
//4
db.product.find({'prodName':'LEDTV', 'quantity':30});

//drop collection
db.product.remove({})
db.product.drop()
db.dropDatabase()