if (process.env.DATABASE_URL) {
    const Sequelize = require("sequelize");
    const db = {};
    const sequelize = new Sequelize(process.env.DATABASE_URL, {
        dialect: 'postgres',
        protocol: 'postgres',

        pool: {
            max: 5,
            min: 0,
            acquire: 30000,
            idle: 10000
        }

    });
    console.log("PostgreSQL Connected on heroku!");
    db.sequelize = sequelize;
    db.Sequelize = Sequelize;

    module.exports = db;
} else {
    const Sequelize = require("sequelize");
    const db = {};
        const sequelize = new Sequelize("predicting_handwriting", "arthurdoelp", "", {
            host: 'localhost',
            dialect: 'postgres',
    
            pool: {
                max: 5,
                min: 0,
                acquire: 30000,
                idle: 10000
            }
    
        });
        console.log("PostgreSQL Connected!");
    
        db.sequelize = sequelize;
        db.Sequelize = Sequelize;
    
    module.exports = db;
}