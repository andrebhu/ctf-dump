const LEADERBOARD_FUNCTION = 'listy';
const LEADERBOARD_PROJECT = 'sunshine-2022-challenges'
const BUCKET_NAME = 'ssctf22-listy-leaderboard-prod'
const LOCAL_DEV = true ? process.env.LOCAL_DEV : false;
export default async (req, res) => {
    if (LOCAL_DEV) {
        res.status(200).json([{
            "rank": 1,
            "username": "Bill",
            "points": 100
        }, {
            "rank": 2,
            "username": "SpongeBob",
            "points": 50
        }])
        return
    }

    const response = await fetch(`https://us-central1-${LEADERBOARD_PROJECT}.cloudfunctions.net/${LEADERBOARD_FUNCTION}?bucket=${BUCKET_NAME}`, {
        headers: {
            Authorization: `bearer ${process.env.GCLOUD_TOKEN}`,
        }
    })
    try {
        console.log('response', response)
        const data = await response.json();
        res.status(200).json(data);
    } catch (e) {
        if (e.message.includes("accounts.google.com")) {
            res.status(401).json({
                error: "Backend Authentication Error."
            })
        } else {
            res.status(500).json({
                error: e
            });
        }
    }
}