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
    // Insert current time + 2 hours into the database
    await connection.execute("INSERT INTO spotify (datetime_column) VALUES (DATE_ADD(NOW(), INTERVAL 2 HOUR))");
    await connection.end();

    return {
      statusCode: 200,
      body: 'Current time (+2 hours) added successfully!',
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: `Database error: ${error.message}`,
    };
  }
};
