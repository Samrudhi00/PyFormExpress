import { Request, Response } from 'express';
import fs from 'fs';
import { app, dbPath } from './server';

app.get('/read', (req: Request, res: Response) => {
    const index = parseInt(req.query.index as string);
    const data = JSON.parse(fs.readFileSync(dbPath, 'utf-8'));

    try {
        if (index < 0 || index >= data.length) {
            throw new Error('Submission not found');
        }
        res.send(data[index]);
    } catch (error: any) {
        console.error(`Error reading submission: ${error.message}`); // Log error using console.error
        res.status(404).send({ error: 'Submission not found' });
    }
});
