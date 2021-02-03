const express = require('express');
const router = express.Router();

//Load Controllers
const {
    newPredictionController,
} = require('../controllers/predict.controller.js')


router.post('/predict/new', newPredictionController);

module.exports = router;