

use studentDB



db.student.insert({

    rollNO: "1BM18CS027",

    name: "Dhanraj K",

    age: 20,

    contactNo: 9686425245,

   emailId: "dhanraj.cs18@bmsce.ac.in"

}) 

db.student.remove({rollNO: "1BM18CS027"})





// 1

db.student.insert({

    rollNO: "1BM18CS027",

    name: "Dhanraj K",

    age: 20,

    contactNo: 9686425245,

   emailId: "dhanraj.cs18@bmsce.ac.in"

}) 

// 2

db.student.insert({

    rollNO: "1BM18CS001",

    name: "abc",

    age: 20,

    contactNo: 9684425245,

   emailId: "abc.cs18@bmsce.ac.in"

}) 

//3

db.student.insert({

    rollNO: "1BM18CS099",

    name: "xyz",

    age: 20,

    contactNo: 9686425333,

   emailId: "xyz.cs18@bmsce.ac.in"

}) 





// to show values inserted in collections

db.student.find()

//show one value

db.student.find({"rollNO": "1BM18CS001"})

//formatted

db.student.find().pretty()





// update value

db.student.update({"rollNO": "1BM18CS001"}, {$set: { "name": "aaa", "emailId": "aaa1@bmsce.ac.in"}})

db.student.find({"rollNO": "1BM18CS001"})



//

db.student.insert({

    rollNO: "11",

    name: "ABC",

    age: 20,

    contactNo: 5686425333,

   emailId: "ABC.cs18@bmsce.ac.in"

})



// db.student.update({"rollNO": "11"}, {$set: {"name": "FEM"}})

db.student.update({"_id": ObjectId("60680e825d06d3ac987a8c17")},{$set: {"name": "FEM"}})

//print

db.student.find({"rollNO": "11"})



// all objects



db.student.find().pretty()



//export and import

// mongoexport --db=studentDB --collection=student --type=csv --fields=rollNO,age,contactNo,emailId --out=C:\Users\dhanr\Desktop\WEEK3\studentinfo.csv
// mongoimport -d studentDB -c student --type csv --file C:\Users\dhanr\Desktop\WEEK3\studimp.csv --headerline

//drop collection

db.student.drop()

//drop database

db.dropDatabase()

