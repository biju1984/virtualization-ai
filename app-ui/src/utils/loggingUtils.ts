import { generateTraceId, getSessionId } from './traceUtils';

export const logUserAction = (action: string) => {
  const traceId = generateTraceId();
  const sessionId = getSessionId();
  console.log(`User action: ${action}, Trace ID: ${traceId}, Session ID: ${sessionId}`);
};
