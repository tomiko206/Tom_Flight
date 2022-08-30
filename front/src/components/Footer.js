import React from 'react';
import './Footer.css';
import { Link } from 'react-router-dom';

function Footer() {
  return (
    <div className='footer-container'>
        <div className='social-media-wrap'>
          <div className='footer-logo'>
            <Link to='/' className='social-logo'>
              Contact Us
              <i className='fab fa-typo3' />
            </Link>
          </div>
          <small className='website-rights'>Flight Project </small>
          <div className='social-icons'>
            <a
              className='social-icon-link facebook'
              href='https://www.facebook.com/tom.elad/'
              target='_blank'
              rel="noopener noreferrer"
              aria-label='Facebook'
            >
              <i className='fab fa-facebook-f' />
              </a>
            <a
              className='social-icon-link docker'
              href='https://hub.docker.com/'
              target='_blank'
              rel="noopener noreferrer"
              aria-label='docker'
            >
              <i className='fab fa-docker' />
            </a>
            <a
              className='social-icon-link github'
              href='https://github.com/'
              target='_blank'
              rel="noopener noreferrer"
              aria-label='github'
            >
              <i className='fab fa-github' />
            </a>
            <a
              className='social-icon-link linkedin'
              href='https://www.linkedin.com/'
              target='_blank'
              rel="noopener noreferrer"
              aria-label='LinkedIn'
            >
              <i className='fab fa-linkedin' />
            </a>
          </div>
        </div>
    </div>
  );
}

export default Footer;
