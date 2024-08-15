import { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const { description } = req.body;
    const response = await fetch('http://localhost:8000/api/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ description }),
    });

    const data = await response;
    console.log(data);
    // res.status(response.status).body(data);
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}
