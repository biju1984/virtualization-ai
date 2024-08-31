
import { useEffect } from 'react';

export const usePerformanceMonitoring = (componentName: string) => {
  useEffect(() => {
    const start = performance.now();

    return () => {
      const end = performance.now();
      console.log(`${componentName} rendered in ${end - start} ms`);
    };
  }, [componentName]);
};
