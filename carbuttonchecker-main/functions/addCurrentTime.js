// addCurrentTime.js
const mysql = require('mysql2/promise');

exports.handler = async function (event) {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: 'Method Not Allowed',
    };
  }

  const connection = await mysql.createConnection({
    host: 'sql7.freesqldatabase.com',
    user: 'sql7756369',
    database: 'sql7756369',
    password: 'DVTT8SsgWT',
  });

  try {
    await connection.execute("INSERT INTO car (datetime_column) VALUES (NOW())");
    await connection.end();

    return {
      statusCode: 200,
      body: 'Current time added successfully!',
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: `Database error: ${error.message}`,
    };
  }
};
