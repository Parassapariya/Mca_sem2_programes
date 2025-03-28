import React from 'react';
import AboutUsFun from "./Component/AboutUsFun";
import Counter from "./Component/Counter";
import EventDemo from "./Component/EventDemo";
import HeaderFun from "./Component/HeaderFun";
import HomeClass from "./Component/HomeClass";
import {BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import HookCounter from "./Component/HooksDemo/HookCounter";
import HookSum from "./Component/HooksDemo/HookSum";
import styled from 'styled-components';

// Styled components
const AppContainer = styled.div`
  display: flex;
  flex-direction: column;
  min-height: 100vh;
`;

const NavBar = styled.nav`
  background: #2c3e50;
  padding: 1rem 2rem;
`;

const NavList = styled.ul`
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: center;
  }
`;

const NavItem = styled.li`
  margin-right: 1.5rem;

  @media (max-width: 768px) {
    margin-right: 0;
    margin-bottom: 0.5rem;
  }
`;

const NavLink = styled(Link)`
  color: #ecf0f1;
  text-decoration: none;
  font-size: 1.1rem;
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;

  &:hover {
    background: #34495e;
    color: #fff;
  }

  &.active {
    background: #3498db;
    color: white;
  }
`;

const MainContent = styled.main`
  flex: 1;
  padding: 2rem;
`;

const FooterContainer = styled.footer`
  background: #2c3e50;
  color: #ecf0f1;
  padding: 2rem;
  text-align: center;
`;

const FooterContent = styled.div`
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  text-align: left;

  @media (max-width: 768px) {
    grid-template-columns: 1fr;
    text-align: center;
  }
`;

const FooterSection = styled.div`
  h3 {
    color: #3498db;
    margin-bottom: 1rem;
    font-size: 1.3rem;
  }

  p {
    margin-bottom: 0.5rem;
    line-height: 1.6;
  }
`;

const FooterLinks = styled.ul`
  list-style: none;
  padding: 0;

  li {
    margin-bottom: 0.5rem;
  }

  a {
    color: #bdc3c7;
    text-decoration: none;
    transition: color 0.3s ease;

    &:hover {
      color: #3498db;
    }
  }
`;

const SocialIcons = styled.div`
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
  justify-content: ${props => props.center ? 'center' : 'flex-start'};

  @media (max-width: 768px) {
    justify-content: center;
  }

  a {
    color: #ecf0f1;
    font-size: 1.5rem;
    transition: color 0.3s ease;

    &:hover {
      color: #3498db;
    }
  }
`;

const Copyright = styled.div`
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid #34495e;
  font-size: 0.9rem;
  color: #bdc3c7;
`;

function FooterFun() {
  return (
    <FooterContainer>
      <FooterContent>
        <FooterSection>
          <h3>About Us</h3>
          <p>We create amazing React applications with modern technologies and best practices.</p>
          <SocialIcons>
            <a href="#"><i className="fab fa-facebook"></i></a>
            <a href="#"><i className="fab fa-twitter"></i></a>
            <a href="#"><i className="fab fa-linkedin"></i></a>
            <a href="#"><i className="fab fa-github"></i></a>
          </SocialIcons>
        </FooterSection>

        <FooterSection>
          <h3>Quick Links</h3>
          <FooterLinks>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/aboutus">About Us</Link></li>
            <li><Link to="/counter">Counter Demo</Link></li>
            <li><Link to="/hookcounter">Hooks Demo</Link></li>
          </FooterLinks>
        </FooterSection>

        <FooterSection>
          <h3>Contact Info</h3>
          <p><i className="fas fa-map-marker-alt"></i> 123 React Street, Component City</p>
          <p><i className="fas fa-phone"></i> +1 (555) 123-4567</p>
          <p><i className="fas fa-envelope"></i> info@reactapp.com</p>
        </FooterSection>
      </FooterContent>

      <Copyright>
        &copy; {new Date().getFullYear()} React App. All rights reserved.
      </Copyright>
    </FooterContainer>
  );
}

function App(props) {
  return (
    <Router>
      <AppContainer>
       
        <NavBar>
          <NavList>
            <NavItem>
              <NavLink to="/">Home</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/aboutus">About Us</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/btnclick">Event Demo</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/counter">Counter</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/hookcounter">Hooks Counter</NavLink>
            </NavItem>
            <NavItem>
              <NavLink to="/hooksum">Hooks Sum</NavLink>
            </NavItem>
          </NavList>
        </NavBar>

        <MainContent>
          <Routes>
            <Route path="/" element={<HomeClass/>}/> 
            <Route path="/aboutus" element={<AboutUsFun/>}/>
            <Route path="/btnclick" element={<EventDemo/>}/>
            <Route path="/counter" element={<Counter/>}/>
            <Route path="/hookcounter" element={<HookCounter/>}/>
            <Route path="/hooksum" element={<HookSum />}/>
          </Routes>
        </MainContent>
        
        <FooterFun />
      </AppContainer>
    </Router>
  );
}

export default App;