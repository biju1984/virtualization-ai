import { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  if (req.method === 'POST') {
    const formData = new FormData();

    req.body.files.forEach((file: File) => {
      formData.append('files', file);
    });

    const response = await fetch('http://localhost:8000/api/upload', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    res.status(response.status).json(data);
  } else {
    res.status(405).json({ message: 'Method not allowed' });
  }
}
