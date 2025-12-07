import { motion } from "framer-motion"
import { ArrowDown, FileText, Github } from "lucide-react"
import { Button } from "@/components/ui/button"
import { PROFILE } from "@/data/profile"

export const Hero = () => {
    return (
        <section id="hero" className="min-h-[80vh] flex flex-col justify-center pt-16">
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
                className="space-y-6"
            >
                <div className="space-y-2">
                    <h2 className="text-xl md:text-2xl font-mono text-primary">Hi there, I'm</h2>
                    <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold tracking-tight">
                        {PROFILE.name}
                    </h1>
                    <h3 className="text-2xl md:text-4xl lg:text-5xl font-bold text-muted-foreground">
                        {PROFILE.role}
                    </h3>
                </div>

                <p className="max-w-[600px] text-lg text-muted-foreground md:text-xl leading-relaxed">
                    Specializing in Data Validation Frameworks, Python Automation, and reconciling complex datasets across files and databases.
                </p>

                <div className="flex flex-col sm:flex-row gap-4 pt-4">
                    <Button size="lg" className="gap-2" onClick={() => document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' })}>
                        View My Work <ArrowDown className="h-4 w-4" />
                    </Button>
                    <div className="flex gap-2">
                        <Button variant="outline" size="lg" className="gap-2" onClick={() => window.open(PROFILE.social.github, '_blank')}>
                            <Github className="h-4 w-4" /> GitHub
                        </Button>
                        <Button variant="outline" size="lg" className="gap-2">
                            <FileText className="h-4 w-4" /> Resume
                        </Button>
                    </div>
                </div>
            </motion.div>
        </section>
    )
}
