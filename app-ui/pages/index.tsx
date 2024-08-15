import React from 'react';
import Link from 'next/link';
import { Box, Typography, Button } from '@mui/material';
import Layout from '../components/Layout';

const HomePage: React.FC = () => {
  return (
    <Layout>
      <Box sx={{ p: 2 }}>
        <Typography variant="h3" gutterBottom>Welcome to API Mockup Tool</Typography>
        <Typography variant="body1" gutterBottom>
          This tool helps you create and refine API specifications using natural language inputs or file uploads.
        </Typography>
        <Box sx={{ mt: 2 }}>
          <Link href="/create" passHref>
            <Button variant="contained" color="primary" sx={{ mr: 2 }}>Create New API</Button>
          </Link>
          <Link href="/modify" passHref>
            <Button variant="contained" color="secondary">Modify Existing API</Button>
          </Link>
        </Box>
      </Box>
    </Layout>
  );
};

export default HomePage;
