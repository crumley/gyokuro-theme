// Gyokuro Theme - JavaScript Sample
import { useState, useEffect } from "react";
import axios from "axios";

/**
 * Fetch and display user data
 * @param {string} userId - The user's unique identifier
 * @returns {Promise<Object>} User data object
 */
async function fetchUserData(userId) {
  try {
    const response = await axios.get(`/api/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error("Error fetching user:", error.message);
    throw error;
  }
}

class ThemeManager {
  constructor(defaultTheme = "gyokuro-desert") {
    this.theme = defaultTheme;
    this.accents = ["cyan", "pink", "orange", "lime", "purple"];
  }

  applyAccent(color) {
    const validColors = ["cyan", "pink", "orange", "lime", "purple"];
    if (!validColors.includes(color)) {
      throw new Error(`Invalid accent color: ${color}`);
    }
    this.currentAccent = color;
    return `${this.theme}-${color}`;
  }
}

// React Component Example
const Dashboard = ({ userId }) => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const REFRESH_INTERVAL = 5000;

  useEffect(() => {
    const loadData = async () => {
      setLoading(true);
      const data = await fetchUserData(userId);
      setUserData(data);
      setLoading(false);
    };

    loadData();
    const interval = setInterval(loadData, REFRESH_INTERVAL);

    return () => clearInterval(interval);
  }, [userId]);

  return loading ? <Spinner /> : <UserProfile data={userData} />;
};

// Regular expressions and template literals
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const welcomeMessage = `Welcome to Gyokuro Theme! 🍵`;

export { fetchUserData, ThemeManager, Dashboard, EMAIL_REGEX };
