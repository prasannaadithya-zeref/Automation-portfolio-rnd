export const Footer = () => {
    return (
        <footer className="py-6 border-t bg-muted/30">
            <div className="container mx-auto px-4 text-center text-sm text-muted-foreground">
                <p>© {new Date().getFullYear()} Prasanna Adithya. All rights reserved.</p>
                <p className="mt-2">Built with React, Tailwind CSS, and Framer Motion.</p>
            </div>
        </footer>
    )
}
