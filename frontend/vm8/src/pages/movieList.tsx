// MoviesList.tsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Movie } from './Movie';

const MoviesList: React.FC = () => {
  const [movies, setMovies] = useState<Movie[]>([]);

  useEffect(() => {
    fetchMovies();
  }, []);

  const fetchMovies = async () => {
    try {
      const response = await axios.get<Movie[]>('http://127.0.0.1:8000/api/movies/');
      setMovies(response.data);
    } catch (error) {
      console.error('Error fetching movies:', error);
    }
  };

  return (
    <div>
      <h1>Movies List</h1>
      <ul>
        {movies.map((movie, index) => (
          <li key={index}>
            <p color={'red'}>{movie.main_title}</p>
            <p>{movie.link_to_the_movie}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MoviesList;
