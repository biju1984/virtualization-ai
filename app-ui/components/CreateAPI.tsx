import React, { useState } from 'react';
import { TextField, Button, Box, Typography, Paper } from '@mui/material';

const CreateAPI: React.FC = () => {
  const [description, setDescription] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState('');

  const handleDescriptionChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setDescription(e.target.value);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (description) {
      const response = await fetch('http://0.0.0.0:8000/api/process_natural_language', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ description }),
      });
      const data = await response.json();
      setResult(data.specification);
    } else if (file) {
      const formData = new FormData();
      formData.append('file', file);
      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data.specification);
    }
  };

  return (
    <Box sx={{ maxWidth: 600, mx: 'auto', p: 2 }}>
      <Paper elevation={3} sx={{ p: 3 }}>
        <Typography variant="h5" gutterBottom>Create New API</Typography>
        <form onSubmit={handleSubmit}>
          <TextField
            label="Description"
            fullWidth
            variant="outlined"
            value={description}
            onChange={handleDescriptionChange}
            sx={{ mb: 2 }}
          />
          <input type="file" onChange={handleFileChange} style={{ display: 'none' }} id="file-upload" />
          <label htmlFor="file-upload">
            <Button variant="contained" component="span" sx={{ mb: 2 }}>Upload File</Button>
          </label>
          <Button type="submit" variant="contained" color="primary">Submit</Button>
        </form>
        {result && (
          <Paper sx={{ mt: 4, p: 2 }}>
            <Typography variant="h6">Generated Specification:</Typography>
            <pre>{result}</pre>
          </Paper>
        )}
      </Paper>
    </Box>
  );
};

export default CreateAPI;
