const { Router } = require("express");
const router = Router();

router.get('/test', (req, res) => {
    const data = {
        "name": "Funciona",
        "website": "Funciona.com"
    };
    res.json(data);
});

module.exports = router;