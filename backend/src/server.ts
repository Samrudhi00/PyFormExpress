// Update error handling in server.ts
import express, { Application, Request, Response } from 'express';
import cors from 'cors';
import fs, { writeFile } from 'fs';

const app: Application = express();
const PORT: number = 3000;
const dbPath: string = './src/db.json';

// Middleware
app.use(express.json());
app.use(cors());

// Logger function
const logger = (msg: string): void => {
    console.error(msg); // Use console.error for logging errors
};

// Read submissions from db.json
let submissions: any[] = [];
try {
    const data = fs.readFileSync(dbPath, 'utf-8');
    submissions = JSON.parse(data);
} catch (err: any) {
    logger(`Error reading db.json: ${err.message}`);
}

// GET endpoint to read all submissions
app.get('/read_all', (req: Request, res: Response) => {
    res.json(submissions);
});

// POST endpoint to submit a new entry
app.post('/submit', (req: Request, res: Response) => {
    const newSubmission = req.body;
    newSubmission.id = submissions.length + 1;
    submissions.push(newSubmission);

    // Update db.json file
    fs.writeFile(dbPath, JSON.stringify(submissions), (err: NodeJS.ErrnoException | null) => {
        if (err) {
            logger(`Error writing to db.json: ${err.message}`);
            res.status(500).json({ error: 'Failed to update submission' });
        } else {
            res.status(201).json(newSubmission);
        }
    });
});

// PUT endpoint to update a submission by ID
app.put('/submit', (req: Request, res: Response) => {
    const updatedSubmission = req.body;
    const index = submissions.findIndex((s) => s.id === updatedSubmission.id);

    if (index !== -1) {
        submissions[index] = updatedSubmission;

        // Update db.json file
        fs.writeFile(dbPath, JSON.stringify(submissions), (err: NodeJS.ErrnoException | null) => {
            if (err) {
                logger(`Error writing to db.json: ${err.message}`);
                res.status(500).json({ error: 'Failed to update submission' });
            } else {
                res.status(200).json(updatedSubmission);
            }
        });
    } else {
        res.status(404).send('Submission not found');
    }
});

// DELETE endpoint to delete a submission by ID
app.delete('/delete', (req: Request, res: Response) => {
    const id = Number(req.query.id);
    const index = submissions.findIndex((s) => s.id === id);

    if (index !== -1) {
        submissions.splice(index, 1);

        // Update db.json file
        fs.writeFile(dbPath, JSON.stringify(submissions), (err: NodeJS.ErrnoException | null) => {
            if (err) {
                logger(`Error writing to db.json: ${err.message}`);
                res.status(500).json({ error: 'Failed to delete submission' });
            } else {
                res.status(200).send('Submission deleted successfully');
            }
        });
    } else {
        res.status(404).send('Submission not found');
    }
});

// Start the server
app.listen(PORT, () => {
    logger(`Server is running on http://localhost:${PORT}`);
});

// Export app and dbPath for use in other modules
export { app, dbPath, logger };
