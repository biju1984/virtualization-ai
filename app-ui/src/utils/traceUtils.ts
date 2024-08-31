import { v4 as uuidv4 } from 'uuid';

export const generateTraceId = (): string => {
  return uuidv4();
};

export const getSessionId = (): string => {
  let sessionId = sessionStorage.getItem('session_id');
  if (!sessionId) {
    sessionId = uuidv4();
    sessionStorage.setItem('session_id', sessionId);
  }
  return sessionId;
};
