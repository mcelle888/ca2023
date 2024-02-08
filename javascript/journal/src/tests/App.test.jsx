import '@testing-library/jest-dom'
import { render, screen } from "@testing-library/react";
import { describe, expect, it, beforeEach } from "vitest";
import App from "../components/App";
import userEvent from '@testing-library/user-event';

describe('App Component', () => {
    let document
  
    beforeEach(()=> {
       document = render(<App />).container
    })
    
    it('renders the Home component', ()=> {

        expect(document.querySelector('h3')).toHaveTextContent('Journal Entries')
    })


    it('renders CategorySelection when Create Entry menu item is clicked', async () => {

        await userEvent.click(screen.getByText('Create Entry'))

        expect(document.querySelector('h3')).not.toBeNull()
        expect(document.querySelector('h3')).toHaveTextContent('Please select a category:')
    })
})