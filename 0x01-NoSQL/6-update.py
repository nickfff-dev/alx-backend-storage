// Add the attribute 'address' with the value '972 Mission street' to all documents in the 'school' collection where name is 'Holberton school'
db.school.update(
 { name: "Holberton school" },
 { $set: { address: "972 Mission street" } },
 { multi: true }
);
