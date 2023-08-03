import Error404 from 'containers/errors/error404';
import Home from 'containers/pages/home';
import { Provider } from 'react-redux';
import store from 'store';
import './App.css';
import { BrowserRouter as Router, Route, Switch, Routes } from 'react-router-dom';

function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="*" element={<Error404 />} />
        </Routes>
      </Router>  
    </Provider>
  );
}

export default App;
