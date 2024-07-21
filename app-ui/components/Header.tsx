import React from 'react';
import Link from 'next/link';

const Header: React.FC = () => {
  return (
    <header className="bg-gray-800 text-white p-4">
      <nav className="container mx-auto flex justify-between">
        <div className="text-xl">MyApp</div>
        <div>
          <Link href="/">
            <a className="mx-2">Home</a>
          </Link>
          <Link href="/products">
            <a className="mx-2">Products</a>
          </Link>
          <Link href="/profile">
            <a className="mx-2">Profile</a>
          </Link>
        </div>
      </nav>
    </header>
  );
};

export default Header;
